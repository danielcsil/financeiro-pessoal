import { computed, ref } from "vue";
import { defineStore } from "pinia";

import { api } from "@/shared/services/api";

/**
 * Estrutura do usuário autenticado retornado pela API.
 *
 * Caso o backend evolua (ex.: avatar, roles, etc.)
 * basta complementar esta interface.
 */
export interface AuthUser {
  id: string;
  name: string;
  email: string;
}

/**
 * Chave utilizada para persistência do JWT.
 *
 * Toda a aplicação deve utilizar SOMENTE esta store para
 * acessar o token.
 */
const TOKEN_STORAGE_KEY = "access_token";

export const useAuthStore = defineStore("auth", () => {
  /**
   * JWT utilizado nas requisições autenticadas.
   */
  const accessToken = ref<string | null>(null);

  /**
   * Usuário autenticado.
   */
  const user = ref<AuthUser | null>(null);

  /**
   * Indica se existe um usuário autenticado.
   */
  const isAuthenticated = computed(() => !!accessToken.value);

  /**
   * Configura o Authorization padrão do Axios.
   *
   * Dessa forma todas as próximas requisições utilizarão
   * automaticamente o JWT.
   */
  function setAuthorizationHeader(token: string) {
    api.defaults.headers.common.Authorization = `Bearer ${token}`;
  }

  /**
   * Remove o Authorization do Axios.
   *
   * Deve ser chamado sempre durante o logout.
   */
  function removeAuthorizationHeader() {
    delete api.defaults.headers.common.Authorization;
  }

  /**
   * Persiste o token na aplicação.
   *
   * Centralizar esta lógica evita que outros componentes
   * manipulem diretamente o localStorage.
   */
  function saveToken(token: string) {
    accessToken.value = token;

    localStorage.setItem(TOKEN_STORAGE_KEY, token);

    setAuthorizationHeader(token);
  }

  /**
   * Remove completamente a sessão atual.
   */
  function clearSession() {
    accessToken.value = null;
    user.value = null;

    localStorage.removeItem(TOKEN_STORAGE_KEY);

    removeAuthorizationHeader();
  }

  /**
   * Realiza autenticação do usuário.
   *
   * Fluxo:
   * 1. Chama a API.
   * 2. Salva o JWT.
   * 3. Carrega o usuário autenticado.
   */
  async function login(email: string, password: string) {
    const { data } = await api.post("/auth/login", {
      email,
      password,
    });

    saveToken(data.access_token);

    await loadCurrentUser();
  }

  /**
   * Busca o usuário autenticado.
   *
   * Caso o token seja inválido ou expirado,
   * a sessão é encerrada automaticamente.
   */
  async function loadCurrentUser() {
    try {
      const { data } = await api.get<AuthUser>("/auth/me");

      user.value = data;
    } catch (error) {
      logout();

      throw error;
    }
  }

  /**
   * Restaura uma sessão persistida.
   *
   * Deve ser executado apenas uma vez durante
   * a inicialização da aplicação.
   */
  async function restoreSession() {
    const token = localStorage.getItem(TOKEN_STORAGE_KEY);

    if (!token) {
      return;
    }

    saveToken(token);

    try {
      await loadCurrentUser();
    } catch {
      // A própria loadCurrentUser já limpa a sessão.
    }
  }

  /**
   * Encerra a sessão do usuário.
   *
   * Remove:
   * - JWT
   * - usuário
   * - localStorage
   * - Authorization do Axios
   */
  function logout() {
    clearSession();
  }

  return {
    // Estado
    accessToken,
    user,

    // Getters
    isAuthenticated,

    // Actions
    login,
    logout,
    loadCurrentUser,
    restoreSession,
  };
});
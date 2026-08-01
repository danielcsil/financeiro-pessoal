import type { NavigationGuardWithThis } from "vue-router";

import { useAuthStore } from "@/modules/auth/stores/auth.store";

/**
 * Indica se a sessão já foi restaurada.
 *
 * O objetivo é evitar chamadas repetidas ao endpoint
 * GET /api/auth/me a cada navegação.
 */
let sessionRestored = false;

/**
 * Guard global responsável pela autenticação.
 *
 * Fluxo:
 *
 * 1. Na primeira navegação restaura uma eventual sessão
 *    persistida no navegador.
 *
 * 2. Verifica se a rota atual exige autenticação através
 *    da propriedade meta.requiresAuth.
 *
 * 3. Caso o usuário não esteja autenticado, redireciona
 *    para a tela de login preservando a rota originalmente
 *    solicitada.
 *
 * Toda a lógica de autenticação permanece centralizada
 * na AuthStore. O Router apenas consulta seu estado.
 */
export const authGuard: NavigationGuardWithThis<undefined> = async (to) => {
  const auth = useAuthStore();

  /**
   * A restauração da sessão acontece apenas uma vez durante
   * todo o ciclo de vida da aplicação.
   */
  if (!sessionRestored) {
    sessionRestored = true;

    try {
      await auth.restoreSession();
    } catch {
      /**
       * Nenhuma ação é necessária.
       *
       * Caso o token seja inválido ou expirado, a própria
       * AuthStore já realiza o logout automaticamente.
       */
    }
  }

  /**
   * Rotas públicas sempre são permitidas.
   */
  if (!to.meta.requiresAuth) {
    return true;
  }

  const guestOnlyRoutes = ["login", "register"];

  if (
      auth.isAuthenticated &&
      guestOnlyRoutes.includes(String(to.name))
  ) {
      return {
          name: "dashboard",
      };
  }

  /**
   * Usuário autenticado pode acessar normalmente.
   */
  if (auth.isAuthenticated) {
    return true;
  }

  /**
   * Usuário não autenticado.
   *
   * Redireciona para o login preservando a rota desejada
   * para possível retorno após autenticação.
   */
  return {
    name: "login",
    query: {
      redirect: to.fullPath,
    },
  };
};
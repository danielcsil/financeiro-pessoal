import { authApi } from "../api/auth.api";

import type { LoginRequest } from "../dto/login-request";
import type { LoginResponse } from "../dto/login-response";
import type { RegisterRequest } from "../dto/register-request";
import type { RegisterResponse } from "../dto/register-response";

class AuthService {
  /**
   * Realiza o cadastro de um novo usuário.
   */
  async register(
    request: RegisterRequest,
  ): Promise<RegisterResponse> {
    return authApi.register(request);
  }

  /**
   * Realiza a autenticação.
   */
  async login(
    request: LoginRequest,
  ): Promise<LoginResponse> {
    return authApi.login(request);
  }

  /**
   * Obtém o usuário autenticado.
   */
  async me() {
    return authApi.me();
  }

  /**
   * Encerra a sessão.
   */
  async logout(): Promise<void> {
    await authApi.logout();
  }
}

export const authService = new AuthService();
import { http } from "@/shared/api";

import type { LoginRequest } from "../dto/login-request";
import type { LoginResponse } from "../dto/login-response";
import type { RegisterRequest } from "../dto/register-request";
import type { RegisterResponse } from "../dto/register-response";

class AuthApi {
  /**
   * Cadastro de usuário.
   */
  async register(
  request: RegisterRequest,
): Promise<RegisterResponse> {
  const { data } = await http.post<RegisterResponse>(
    "/auth/register",
    {
      name: request.name,
      email: request.email,
      password: request.password,
      password_confirmation: request.passwordConfirmation,
      accept_terms: request.acceptTerms,
    },
  );

  return data;
}

  /**
   * Autenticação.
   */
  async login(
    request: LoginRequest,
  ): Promise<LoginResponse> {
    const { data } = await http.post<LoginResponse>(
      "/auth/login",
      {
        email: request.email,
        password: request.password,
      },
    );

    return data;
  }

  /**
   * Obtém o usuário autenticado.
   */
  async me() {
    const { data } = await http.get("/auth/me");

    return data;
  }

  /**
   * Logout.
   *
   * Nesta primeira versão o backend não possui endpoint
   * específico. A remoção do token será feita localmente.
   */
  async logout(): Promise<void> {
    return Promise.resolve();
  }
}

export const authApi = new AuthApi();
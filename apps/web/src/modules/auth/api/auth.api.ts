import { http } from "@/shared/api";

import type { RegisterRequest } from "../dto/register-request";
import type { RegisterResponse } from "../dto/register-response";
import type { LoginRequest } from "../dto/login-request";
import type { LoginResponse } from "../dto/login-response";

type AuthUser = {
  id: string;
  name: string;
  email: string;
};

export class AuthApi {
  async register(
    request: RegisterRequest,
  ): Promise<RegisterResponse> {
    const { data } = await http.post<RegisterResponse>(
      "/auth/register",
      {
        name: request.name,
        email: request.email,
        password: request.password,
        password_confirmation:
          request.passwordConfirmation,
        accept_terms: request.acceptTerms,
      },
    );

    return data;
  }

  async login(
    request: LoginRequest,
  ): Promise<LoginResponse> {
    const { data } =
      await http.post<LoginResponse>(
        "/auth/login",
        request,
      );

    return data;
  }

  async me(): Promise<AuthUser> {
    const { data } = await http.get<AuthUser>("/auth/me");

    return data;
  }

  async logout(): Promise<void> {
    await http.post("/auth/logout");
  }
}

export const authApi = new AuthApi();

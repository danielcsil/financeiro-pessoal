import { authApi } from "../api/auth.api";

import type { LoginRequest } from "../dto/login-request";
import type { LoginResponse } from "../dto/login-response";
import type { RegisterRequest } from "../dto/register-request";
import type { RegisterResponse } from "../dto/register-response";

export class AuthService {
  async register(
    request: RegisterRequest,
  ): Promise<RegisterResponse> {
    return authApi.register(request);
  }

  async login(
    request: LoginRequest,
  ): Promise<LoginResponse> {
    return authApi.login(request);
  }

  async me() {
    return authApi.me();
  }

  async logout(): Promise<void> {
    await authApi.logout();
  }
}

export const authService = new AuthService();
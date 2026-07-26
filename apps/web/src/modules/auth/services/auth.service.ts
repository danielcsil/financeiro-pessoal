import { api } from "@/shared/services/api";

export interface RegisterRequest {
  name: string;
  email: string;
  password: string;
  passwordConfirmation: string;
  acceptTerms: boolean;
}

export interface LoginRequest {
  email: string;
  password: string;
}

export interface LoginResponse {
  name: string;
  email: string;
  access_token: string;
}

export async function register(
  request: RegisterRequest,
): Promise<void> {
  await api.post("/auth/register", {
    name: request.name,
    email: request.email,
    password: request.password,
    password_confirmation: request.passwordConfirmation,
    accept_terms: request.acceptTerms,
  });
}

export async function login(
  request: LoginRequest,
): Promise<LoginResponse> {
  const response = await api.post<LoginResponse>(
    "/auth/login",
    request,
  );

  return response.data;
}
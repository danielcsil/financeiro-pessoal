/**
 * Resposta retornada pelo endpoint:
 *
 * POST /api/auth/login
 */
export interface LoginResponse {
  /**
   * Identificador do usuário autenticado.
   */
  id: string;

  /**
   * Nome do usuário.
   */
  name: string;

  /**
   * E-mail do usuário.
   */
  email: string;

  /**
   * JWT utilizado nas requisições autenticadas.
   */
  access_token: string;

  /**
   * Data/hora da autenticação.
   *
   * Formato ISO 8601 retornado pelo backend.
   */
  authenticated_at: string;
}
import type { AuthUser } from "./auth-user";

/**
 * Representa a sessão autenticada da aplicação.
 *
 * Esta interface é utilizada pela camada de aplicação
 * e abstrai completamente o formato retornado pela API.
 */
export interface AuthSession {
  /**
   * Token JWT utilizado nas requisições autenticadas.
   */
  accessToken: string;

  /**
   * Refresh Token utilizado para renovação da sessão.
   *
   * Opcional nesta primeira versão, pois o backend
   * ainda não implementa Refresh Token.
   */
  refreshToken?: string;

  /**
   * Tipo do token.
   *
   * Normalmente "Bearer".
   */
  tokenType: string;

  /**
   * Data/hora de expiração do Access Token.
   *
   * Opcional até implementarmos expiração.
   */
  expiresAt?: Date;

  /**
   * Usuário autenticado.
   */
  user: AuthUser;
}
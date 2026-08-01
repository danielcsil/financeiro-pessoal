/**
 * Representa o usuário autenticado na aplicação.
 *
 * Este modelo é utilizado pela camada de aplicação
 * (Store, Services e Views) e não deve refletir
 * necessariamente o DTO retornado pela API.
 */
export interface AuthUser {
  /**
   * Identificador único do usuário.
   */
  id: string;

  /**
   * Nome completo.
   */
  name: string;

  /**
   * Endereço de e-mail.
   */
  email: string;

  /**
   * Indica se a conta está ativa.
   */
  isActive: boolean;

  /**
   * Indica se o e-mail já foi confirmado.
   */
  emailVerified: boolean;

  /**
   * Data de criação da conta.
   */
  createdAt: Date;

  /**
   * Data da última atualização.
   */
  updatedAt: Date;
}
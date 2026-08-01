export interface RegisterRequest {
  name: string;
  email: string;
  password: string;
  passwordConfirmation: string;
  acceptTerms: boolean;
}
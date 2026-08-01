import axios from "axios";

export function getErrorMessage(error: unknown): string {
  if (!axios.isAxiosError(error)) {
    return "Erro inesperado.";
  }

  const message = error.response?.data?.detail;

  if (typeof message === "string") {
    return message;
  }

  return "Não foi possível concluir a operação.";
}
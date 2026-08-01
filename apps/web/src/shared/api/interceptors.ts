import type { AxiosInstance } from "axios";

import { AuthStorage } from "./auth-storage";

export function setupInterceptors(http: AxiosInstance): void {
  http.interceptors.request.use((config) => {
    const token = AuthStorage.getAccessToken();

    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }

    return config;
  });

  http.interceptors.response.use(
    (response) => response,

    async (error) => {
      /**
       * JWT Refresh Token
       *
       * Ainda não implementaremos.
       *
       * Aqui será feita a renovação automática
       * quando o backend retornar 401.
       */
      return Promise.reject(error);
    },
  );
}
import axios from "axios";

import { setupInterceptors } from "./interceptors";

export const http = axios.create({
  baseURL: "/api",

  headers: {
    "Content-Type": "application/json",
  },

  timeout: 10000,
});

setupInterceptors(http);
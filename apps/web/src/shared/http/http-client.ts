/**
 * ============================================================================
 * HTTP Client
 * ============================================================================
 *
 * Purpose
 * ============================================================================
 *
 * Centralizes every HTTP communication performed by the application.
 *
 * This module exposes a single Axios instance configured with:
 *
 * • Base URL
 * • Timeout
 * • Default headers
 * • Authentication
 * • Error handling
 * • Future request/response interceptors
 *
 * No application module should import Axios directly.
 *
 * ============================================================================
 * Architecture
 * ============================================================================
 *
 * Financial Accounts
 * Authentication
 * Transactions
 * Goals
 * Investments
 * AI
 *
 *          │
 *          ▼
 *
 *      Http Client
 *
 *          │
 *          ▼
 *
 *      Personal Finance API
 *
 * ============================================================================
 * Design Principles
 * ============================================================================
 *
 * • Single HTTP client.
 *
 * • Centralized configuration.
 *
 * • Automatic authentication.
 *
 * • Consistent error handling.
 */

import axios, {
    AxiosError,
    AxiosInstance,
    AxiosRequestConfig,
    InternalAxiosRequestConfig,
} from "axios";

/**
 * Base URL of the backend API.
 *
 * This value should come from Vite environment variables.
 */
const API_URL =
    import.meta.env.VITE_API_URL ??
    "http://localhost:8000/api";

/**
 * Creates the application's HTTP client.
 */
const http: AxiosInstance = axios.create({

    baseURL: API_URL,

    timeout: 10000,

    headers: {

        Accept: "application/json",

        "Content-Type": "application/json",

    },

});


// ============================================================================
// Request Interceptor
// ============================================================================

http.interceptors.request.use(

    (config: InternalAxiosRequestConfig) => {

        const token = localStorage.getItem("access_token");

        if (token) {

            config.headers = config.headers ?? {};

            // ensure header types align
            (config.headers as any).Authorization = `Bearer ${token}`;

        }

        return config;

    },

);


// ============================================================================
// Response Interceptor
// ============================================================================

http.interceptors.response.use(

    response => response,

    (error: AxiosError) => {

        /**
         * Authentication expired.
         */
        if (error.response?.status === 401) {

            localStorage.removeItem(
                "access_token",
            );

            window.location.href = "/login";
        }

        return Promise.reject(
            error,
        );

    },

);


export default http;
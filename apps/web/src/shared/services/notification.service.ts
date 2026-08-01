export type NotificationType =
  | "success"
  | "error"
  | "warning"
  | "info";

export interface Notification {
  type: NotificationType;
  message: string;
}

class NotificationService {
  /**
   * Implementação temporária.
   *
   * Na próxima sprint este serviço será conectado
   * a um componente Toast global.
   */
  notify(notification: Notification): void {
    window.alert(notification.message);
  }

  success(message: string): void {
    this.notify({
      type: "success",
      message,
    });
  }

  error(message: string): void {
    this.notify({
      type: "error",
      message,
    });
  }

  warning(message: string): void {
    this.notify({
      type: "warning",
      message,
    });
  }

  info(message: string): void {
    this.notify({
      type: "info",
      message,
    });
  }
}

export const notificationService =
  new NotificationService();
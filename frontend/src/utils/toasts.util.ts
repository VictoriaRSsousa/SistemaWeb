import app from "../main";

export class Toasts {
  public showError(message?: string, detail?: string) {
    app.config.globalProperties.$toast.add({
      severity: "error",
      summary: message ?? "Failed to connect",
      detail: detail ?? "The connection could not be completed!",
      life: 3000,
    });
  }

  public showSuccess(message?: string, detail?: string) {
    app.config.globalProperties.$toast.add({
      severity: "success",
      summary: message ?? "Success Message",
      detail: detail ?? "Message Content",
      life: 3000,
    });
  }

  public showWarn(message?: string, detail?: string) {
    app.config.globalProperties.$toast.add({
      severity: "warn",
      summary: message ?? "Warn Message",
      detail: detail ?? "Message Content",
      life: 3000,
    });
  }

  public showInfo(message?: string, detail?: string) {
    app.config.globalProperties.$toast.add({
      severity: "info",
      summary: message ?? "Info Message",
      detail: detail ?? "Message Content",
      life: 3000,
    });
  }
}
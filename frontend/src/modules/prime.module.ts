

import Toast from 'primevue/toast';
import ConfirmDialog from 'primevue/confirmdialog';

import type { App } from 'vue';

export default function setPrimeComponent(app: App): void {
    app.component('Toast', Toast);
    app.component('ConfirmDialog',ConfirmDialog)

}
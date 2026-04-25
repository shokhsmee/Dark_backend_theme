/** @odoo-module */

import { Component } from "@odoo/owl";
import { registry } from "@web/core/registry";

class ColorPickerField extends Component {
    static template = "oil_backend_theme.ColorPickerField";
    static props = { "*": true };

    get value() {
        const record = this.props.record;
        if (!record || !this.props.name) return '#FF6A00';
        return record.data[this.props.name] || '#FF6A00';
    }

    onInput(ev) {
        this.props.record.update({ [this.props.name]: ev.target.value });
    }

    onTextInput(ev) {
        const val = ev.target.value;
        if (/^#[0-9A-Fa-f]{6}$/.test(val)) {
            this.props.record.update({ [this.props.name]: val });
        }
    }
}

registry.category("fields").add("oil_hex_color", ColorPickerField);

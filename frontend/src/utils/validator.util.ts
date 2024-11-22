import { helpers } from "@vuelidate/validators";

const validatePhone = helpers.regex(/^\(?\d{2}\)?[-.\s]?\d{4,5}[-.\s]?\d{4}$/)

const validateName  = helpers.regex(/^[a-zA-ZÀ-ÿ]+([a-zA-ZÀ-ÿ' ]*[a-zA-ZÀ-ÿ]+)*$/)

const validateCnpj = helpers.regex(/^(\d{2}\.\d{3}\.\d{3}\/\d{4}-\d{2}|\d{14})$/)

export { validatePhone, validateName, validateCnpj };
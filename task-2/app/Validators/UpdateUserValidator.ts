import { schema, validator, rules } from "@ioc:Adonis/Core/Validator";
import { HttpContextContract } from "@ioc:Adonis/Core/HttpContext";

export default class UpdateAccountValidator {
  constructor(protected ctx: HttpContextContract) {}

  public reporter = validator.reporters.api;

  public schema = schema.create({
    name: schema.string.optional({}, [rules.maxLength(255)]),
    timezone: schema.string.optional({}, [rules.maxLength(255)]),
    birthday: schema.date.optional(),
  });
}

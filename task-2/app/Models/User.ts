import { DateTime } from "luxon";
import {
  BaseModel,
  column,
} from "@ioc:Adonis/Lucid/Orm";

export default class User extends BaseModel {
  @column({ isPrimary: true })
  public id: string;

  @column()
  public name: string;

  @column()
  public timezone: string;

  @column()
  public birthday: string;

  @column()
  public has_congratulated_birthday: boolean;

  @column.dateTime({ autoCreate: true })
  public created_at: DateTime;

  @column.dateTime({ autoCreate: true, autoUpdate: true })
  public updated_at: DateTime;

  @column.dateTime()
  public deleted_at: DateTime;

  static get table() {
    return "users";
  }
}

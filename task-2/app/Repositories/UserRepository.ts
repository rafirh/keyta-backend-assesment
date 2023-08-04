import BaseRepository from "App/Base/Repositories/BaseRepository";
import Account from "App/Models/User";

export default class AccountRepository extends BaseRepository {
  constructor() {
    super(Account);
  }
}

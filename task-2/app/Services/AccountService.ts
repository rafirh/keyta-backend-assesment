import BaseService from "App/Base/Services/BaseService";
import AccountRepository from "App/Repositories/UserRepository";

export default class AccountService extends BaseService {
  constructor() {
    super(new AccountRepository());
  }
}

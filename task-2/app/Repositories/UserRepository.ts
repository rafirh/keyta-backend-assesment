import BaseRepository from "App/Base/Repositories/BaseRepository";
import User from "App/Models/User";

export default class UserRepository extends BaseRepository {
  constructor() {
    super(User);
  }
}

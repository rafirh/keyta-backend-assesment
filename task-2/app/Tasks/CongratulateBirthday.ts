import User from "App/Models/User";
import { BaseTask } from "adonis5-scheduler/build";
import axios from "axios";
import moment from "moment-timezone";

export default class CongratulateBirthday extends BaseTask {
  public static get schedule() {
    return "0 * * * * *";
  }
  /**
   * Set enable use .lock file for block run retry task
   * Lock file save to `build/tmpTaskLock`
   */
  public static get useLock() {
    return false;
  }

  async handle() {
    const today = moment();
    const users = await User.query()
      .whereRaw("MONTH(birthday) = ?", [today.month() + 1])
      .whereRaw("DAY(birthday) BETWEEN ? AND ?", [
        today.date() - 1,
        today.date() + 1,
      ])
      .where("has_congratulated_birthday", false)
      .exec();
    
    for (const user of users) {
      const userTime = today.tz(user.timezone);
      const userBirthday = moment(user.birthday).tz(user.timezone);
      const monthBirthday = userBirthday.month();
      const dateBirthday = userBirthday.date();

      if (userTime.hour() === 9 && userTime.month() === monthBirthday && userTime.date() === dateBirthday) {
        const message = `Hey, ${user.name} it's your birthday!`;
        try {
          await axios.post(
            "https://eo5uccqnfdhmmq7.m.pipedream.net",
            {
              message,
              user_timezone: user.timezone,
            }
          );
          
          User.query().where("id", user.id).update({
            has_congratulated_birthday: true,
          }).exec();

          console.log(`Success send message to ${user.name}`);
        } catch (error) {
          console.log(`Failed send message to ${user.name}`);
        }
      }
    }
  }
}

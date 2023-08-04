import Route from '@ioc:Adonis/Core/Route'

Route.group(function () {
  Route.delete('/', 'UserController.destroyAll').as('users.destroyAll')
}).prefix('users')
Route.resource('users', 'UserController').apiOnly()

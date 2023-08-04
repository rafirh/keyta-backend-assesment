## How to run the project

### 1. Clone the repository
```
git clone https://github.com/rafirh/keyta-backend-assesment.git
cd keyta-backend-assesment/task-2
```

### 2. Install dependencies
```
npm install
```

### 3. Copy .env.example to .env
```
cp .env.example .env
```

### 4. Create database with name `task_2` and run migration
```
node ace migration:run
```

### 5. Run the project
```
npm run dev
```

### 6. Run the scheduler
```
node ace scheduler:run
```

### 7. User endpoint
```
GET http://localhost:3333/api/users
GET http://localhost:3333/api/users/:id
POST http://localhost:3333/api/users
PUT http://localhost:3333/api/users/:id
DELETE http://localhost:3333/api/users/:id
```

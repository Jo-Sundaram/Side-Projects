  
const express = require('express');
const cors = require('cors');
const mongoose = require('mongoose'); 

require('dotenv').config(); // environent vrarables

const app = express();
const port = process.env.PORT || 5000; // create express server

app.use(cors()); // use middle ware
app.use(express.json()); // parse json

const uri = process.env.ATLAS_URI;
mongoose.connect(uri, { useNewUrlParser: true, useCreateIndex: true }
);
const connection = mongoose.connection;
connection.once('open', () => {
  console.log("MongoDB database connection established successfully");
}) 

const exercisesRouter = require('./routes/exercises');
const usersRouter = require('./routes/users'); 
app.use('/exercises', exercisesRouter);
app.use('/users', usersRouter);

app.listen(port, () => {
    console.log(`Server is running on port: ${port}`); // creates server
});
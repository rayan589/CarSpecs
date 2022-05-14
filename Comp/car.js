const mongoose = require('mongoose');

mongoose.connect('mongodb+srv://dbRayan:dbrayan589@bbkar-project.smvmj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority', 
{
    useMongoClient: true
})


const carSchema = mongoose.Schema({
    _id: mongoose.Types.ObjectId,
    brand: String,
    model: String   
});

module.exports = mongoose.model('Car', carSchema);
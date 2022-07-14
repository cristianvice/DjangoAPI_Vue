// import { reject } from 'core-js/fn/promise';
import Dexie from 'dexie';
import Vue from 'vue'

var db = new Dexie('UserDatabase');
db.version(1).stores({ users: "++id, uname, password"});
db.open();

db.users.add({uname: "advay", password: "mehta"})

// const firstFriend =  db.users.get(44);
// console.log("Friend with id 1: " + db.users.toArray());
// const a = await new Promise((resolve, reject)=>{
//     return resolve(db.users.toArray());
// })

db.users.toArray().then(function (arr) {
    // Vue.states.database = arr;
    console.log(arr);
    this.$store.state.data = arr;
});


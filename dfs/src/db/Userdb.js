import { db } from './db';

export class Userdb {

    static getInstance() {
        return new Userdb();
    }

    get() {
        // var a = db.users.toArray().then(function (arr) {
        //     console.log(arr);
        //     return arr;
        // });
        // return a;
    }
}
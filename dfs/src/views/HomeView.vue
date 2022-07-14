<template>
  <div>
    <b-nav tabs>
      <b-nav-item active>Home</b-nav-item>
      <b-nav-item>Post</b-nav-item>
      <b-nav-item>About</b-nav-item>
      <!-- <b-nav-item disabled>Disabled</b-nav-item> -->
      <b-nav-item>User</b-nav-item>
      <b-nav-item>Log Out</b-nav-item>
    </b-nav>

    <div class="vue-tempalte">
      <!-- Navigation -->
      <nav
        class="
          navbar
          shadow
          bg-white
          rounded
          justify-content-between
          flex-nowrap flex-row
          fixed-top
        "
      >
        <div class="container">
          <a
            class="navbar-brand float-left"
            href="https://www.positronx.io"
            target="_blank"
          >
            LOGO MKCL
          </a>
          <a class="navbar-brand float-right" href="" target="_blank"> HOME </a>
          <a class="navbar-brand float-right" href="" target="_blank">
            About
          </a>
          <div v-if="logged">					
            <ul class="nav navbar-nav flex-row float-right">
              <li class="nav-item">
                <router-link class="nav-link pr-3" to="/login"
                  >Sign in</router-link
                >
              </li>
              <li class="nav-item">
                <router-link class="btn btn-outline-primary" to="/registration"
                  >Sign up</router-link
                >
              </li>
            </ul>
          </div>
					<div v-else>
						<ul class="nav navbar-nav flex-row float-right">
						<li class="nav-item">
                <button class="nav-link pr-3"  @click="logout"
                  ><strong>LogOut</strong></button
                >
              </li>
            </ul>
					</div>
        </div>
      </nav>

      <!-- Main -->
      <div class="App">
        <div class="vertical-center">
          <div class="inner-block">
            <button @click="log"> Logg</button>
            <router-view />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
// import LoginPage from '@/views/LoginPage.vue'
// import { Userdb } from "@/db/Userdb.js";
// import { db } from "@/db/db.js";
export default {
  name: "HomeView",

  data() {
    return {
      // users: [
      //   { username: "advay", password: "mehta" },
      //   { username: "nitish", password: "tiwari" },
      //   { username: "mdlucky", password: "lucky" },
      // ],
      users: [],
      logged: true,
      user_api_data : []
    };
  },
  created() {

    
  },
  mounted() {
    this.refreshData();
    // console.log("a", this.$store.state.data);
    //     var us = new Userdb();
    //     Userdb.getInstance()
    //       .get()
    //       .then((result) => {
    //         console.log(result);
    //       });
    //     const a = await us.get();

    //     db.users.toArray().then(function (arr) {
    //     console.log('mounted', arr);
    //     // return arr;
    // });

		console.log("route", this.$route.query.action);
    if (this.$route.query.action == 'login') {
      this.logged = false;
    }
		console.log('log', this.logged)

    this.users = this.$store.state.users;
    console.log("this.usrs:", this.users);
    // console.log("route", this.$route.params.data);
    // if (this.$route.params.data != undefined) {
    //   this.logged = false;
    // }
  },
	methods:{

    refreshData(){
      axios.get(server.API_URL+"blog")
      .then((response)=>{
        this.user_api_data=response.data;
      });

      console.log("API1", this.user_api_data);
    },

		logout(){
			alert('Logged Out');
      console.log("API1", this.user_api_data);
			window.location.reload();
        this.$router.push({
          path: '/',
          params: null
        })
		},

    log(){
      console.log("apppp", this.user_api_data);
    }
	}
};
</script>

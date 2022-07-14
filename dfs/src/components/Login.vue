<template>
  <div class="vue-tempalte">
    <!-- <form>
      <h3>Sign In</h3>

      <div class="form-group">
        <label>Email address</label>
        <input type="email" class="form-control form-control-lg" />
      </div>

      <div class="form-group">
        <label>Password</label>
        <input type="password" class="form-control form-control-lg" />
      </div>

      <button
        type="submit"
        class="btn btn-dark btn-lg btn-block"
        @submit="onSumbit"
      >
        Sign In
      </button>

      <p class="forgot-password text-right mt-2 mb-4">
        <router-link to="/forgot-password">Forgot password ?</router-link>
      </p>
    </form> -->

    <div>
      <b-form @submit="onSubmit" @reset="onReset" v-if="show">
        <b-form-group
          id="input-group-1"
          label="Email address:"
          label-for="input-1"
          description="We'll never share your email with anyone else."
          class="form-control form-control-lg"
        >
          <b-form-input
            id="input-1"
            v-model="form.email"
            type="email"
            placeholder="Enter email"
            required
          ></b-form-input>
        </b-form-group>

        <b-form-group
          id="input-group-2"
          label="Password"
          label-for="input-2"
          description="your password is safe."
          class="form-control form-control-lg"
        >
          <b-form-input
            id="input-2"
            v-model="form.password"
            type="password"
            placeholder="Enter Password"
            required
          ></b-form-input>
        </b-form-group>

        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>

        <p class="forgot-password text-right mt-2 mb-4">
          <router-link to="/forgot-password">Forgot password ?</router-link>
        </p>
      </b-form>

      <b-card class="mt-3" header="Form Data Result">
        <pre class="m-0">{{ form }}</pre>
      </b-card>
    </div>
  </div>
</template>
 
<script>
export default {
  data() {
    return {
      form: {
        email: "",
        //   name: '',
        password: "",
      },
      show: true,
    };
  },

  mounted() {
    // console.log(db);
  },
  methods: {
    onSubmit(event) {
      event.preventDefault();
      // alert(JSON.stringify(this.form))
      console.log(this.form);
      let users = this.$store.state.users;
      let user = users.filter((element) => {
        if (element.username == this.form.email) {
          return true;
        }

        return false;
      })[0];

      // console.log(user[0], this.form.password);
      if(user.password != this.form.password)
      {
        alert('Login Failed');
      }
      else{
        alert('Login Success');
        this.$router.push({
          path: '/',
          query: { data : user , action : 'login' }
        })
      }
      
    },
    onReset(event) {
      event.preventDefault();
      // Reset our form values
      this.form.email = "";
      this.form.password = "";
      // this.form.name = ''
      // Trick to reset/clear native browser form validation state
      this.show = false;
      this.$nextTick(() => {
        this.show = true;
      });
    },
  },
};
</script>
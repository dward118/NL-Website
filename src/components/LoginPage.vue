<template>
  <div>
    <MenuBarLimited />

    <h1 style="font-size:40px; color: #00313c; margin-top: 200px;">Login</h1>
    <div class="field">
      <input type="text" v-model="username"  placeholder="Enter Username" id="username" name="username" required />
      <input type="password"  v-model="password"   placeholder="Enter Password" id="password" name="password" required />
      <button type="submit" v-on:click="login">Log in</button>
      <br />
      <br />
      <router-link to="/sign-up">SignUp</router-link>
    </div>



  </div>
</template>

<script>
import MenuBarLimited from './MenuBarLimited.vue';


export default {
  name: 'LoginPage',

  get(){
    return{
      username:'',
      password:'',
      LoginStatus:false
 
    }
  },
  methods:{
    login(){
      //let result = await axios.post("http://localhost:3000/users",{
       // email:this.email,
      //  username:this.username,
     //   password:this.password
     // });
      
      this.LoginStatus = true;
      console.warn(this.username, this.password);
      console.warn(this.LoginStatus);
      window.location.href = "http://localhost:8081/"


      //if (result.status == 201){
       // alert("sign-up done")
       // localStorage.setItem("user-info",JSON.stringify(result.data))
     // }

    }
  },



  
  components: {
    MenuBarLimited
  },

  data() {
    return {
      activeItem: 'NucScholar',
    };
  },
};
</script>

<style scoped>
.field input {
  width: 300px;
  height: 40px;
  padding-left: 20px;
  display: block;
  margin-bottom: 30px;
  margin-right: auto;
  margin-left: auto;
  border: 1px solid #fac62e;
}

.field button {
  width: 320px;
  height: 40px;
  border: 1px solid #00313c;
  background: #00313c;
  color: #fff;
  cursor: pointer;
}
</style>

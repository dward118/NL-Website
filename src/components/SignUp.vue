<template>
  <div>
    <MenuBarLimited />

   
    <h1 style="font-size:40px; color: #00313c; margin-top: 200px;">Sign Up</h1>
    <div class="field">
      <input type="email" v-model="email" placeholder="Enter Your Email" id="email" name="email" required>
      <input type="text" v-model="username" placeholder="Enter Username" id="username" name="username" required />
      <input type="password"  v-model="password"  placeholder="Enter Password" id="password" name="password" required />
      <button type="submit" v-on:click="signUp" >Submit</button>
    </div>
    <p>
      <router-link to="/login">Login</router-link>
      </p>

  </div>
</template>

<script>
import MenuBarLimited from './MenuBarLimited.vue';
//import axios from 'axios'

export default {
  name: 'SignUp',

  get(){
    return{
      username:'',
      email:'',
      password:''
    }
  },
  methods:{
     signUp(){
      //let result = await axios.post("http://localhost:3000/users",{
       // email:this.email,
      //  username:this.username,
     //   password:this.password
     // });

      console.warn(this.email, this.username, this.password);

      //if (result.status == 201){
       // alert("sign-up done")
       // localStorage.setItem("user-info",JSON.stringify(result.data))
     // }

    }
  },


  components: {
    MenuBarLimited
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
border: 1px solid skyblue;
}

.field button {
width: 320px;
height: 40px;
border: 1px solid skyblue;
background: skyblue;
color: #fff;
cursor: pointer;
}
</style>
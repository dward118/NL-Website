<template>
  <div>
    <MenuBar />

   
    <h1 style="font-size:40px; color: #00313c; margin-top: 150px;">Sign Up</h1>
    <div class="field">
      <input type="email" placeholder="Enter Your Email" id="email" name="email" required>
      <input type="text" placeholder="Enter Username" id="username" name="username" required />
      <input type="password" placeholder="Enter Password" id="password" name="password" required />
      <button type="submit">Submit</button>
      <p>
        <router-link to="/login">Back to Login</router-link>
      </p>
    </div>

  </div>

  <!-- This is to create whitespace at the bottom until we have other containers. -->
  <div style="height: 200px;"></div>
</template>

<script>
import MenuBar from './MenuBar.vue';

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
    MenuBar
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

p {
  text-align: center;
}
</style>
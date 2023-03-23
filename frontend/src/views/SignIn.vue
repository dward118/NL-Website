<template>
  <div>
    <MenuBar />

    <h1 style="font-size:40px; color: #00313c; margin-top: 200px;">Login</h1>
    <div class="field">
      <input type="text" placeholder="Enter Username" id="username" name="username" required />
      <input type="password" placeholder="Enter Password" id="password" name="password" required />
      <button type="submit">Login</button>
      <p>
        <router-link to="/sign-up">Don't have an account? Sign up here.</router-link>
      </p>
    </div>



  </div>

  <!-- This is to create whitespace at the bottom until we have other containers. -->
  <div style="height: 200px;"></div>
</template>

<script>
import MenuBar from '../components/MenuBar.vue';


export default {
  name: 'SignIn',

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

     //None of this is right
     this.LoginStatus = true;

      if (this.LoginStatus){
      console.warn(this.username, this.password);
      console.warn(this.LoginStatus);
      window.location.href = "http://localhost:8080/"
      } else{

        alert('Invalid username/password')
  .then(() => {
    console.log("Alert dialog closed.");
  });

      }

      //if (result.status == 201){
       // alert("sign-up done")
       // localStorage.setItem("user-info",JSON.stringify(result.data))
     // }

    }
  },



  
  components: {
    MenuBar
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
  margin-bottom: 10px;
}
</style>

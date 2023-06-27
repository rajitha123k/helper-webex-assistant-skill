<script>
  import { Router, Route, Link } from 'svelte-routing';
  import Login from './Login.svelte';
  import Meetings from './Meetings.svelte';
  export let url = "/";
</script>
<Router {url}>
  <!-- <nav>
    <Link to="/login">Login</Link>
    <Link to="/meetings">meetings</Link>
  </nav> -->
  <div>
    <Route path="/meetings"><Meetings/></Route>
    <Route path="/login"><Login /></Route>
    <Route path="/"><Login /></Route>
  </div>
</Router>
<style>
  :global(body) {
    font-family: sans-serif;
    margin: 0;
    padding: 0;
  }
</style>
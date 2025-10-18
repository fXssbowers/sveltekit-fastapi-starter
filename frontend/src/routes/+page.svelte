<script lang="ts">
  let message = 'Welcome to SvelteKit';

  async function fetchHello() {
    try {
      const response = await fetch('/api/hello');
      const data = await response.json();
      message = data.message;
    } catch (error) {
      console.error('Error fetching message:', error);
    }
  }
</script>

<main>
  <h1>{message}</h1>
  <p>Visit <a href="https://kit.svelte.dev">kit.svelte.dev</a> to read the documentation</p>
  <button on:click={fetchHello}>Get Message from API</button>
</main>

<style>
  main {
    text-align: center;
    padding: 1em;
    max-width: 240px;
    margin: 0 auto;
  }

  h1 {
    color: #ff3e00;
    text-transform: uppercase;
    font-size: 4em;
    font-weight: 100;
  }

  button {
    font-size: 1.2em;
    padding: 0.5em 1em;
    background: #ff3e00;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }

  button:hover {
    background: #ff5722;
  }

  @media (min-width: 640px) {
    main {
      max-width: none;
    }
  }
</style>

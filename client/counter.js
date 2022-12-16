const { createApp } = Vue

createApp({
  data() {
    return {
      value: "?",
      users: "",
      websocket: new WebSocket("ws://localhost:6789/")
    }
  },
  methods: {
    increment(){
      this.websocket.send(JSON.stringify({ action: "plus" }));
    },
    decrement(){
      this.websocket.send(JSON.stringify({ action: "minus" }));
    }
  },
  mounted(){
    this.websocket.onmessage = ({data}) => {
      const event = JSON.parse(data);
      switch (event.type) {
        case "value":
          this.value = event.value;
          break;
        case "users":
          const users = `${event.count} user${event.count == 1 ? "" : "s"}`;
          this.users = users;
          break;
        default:
          console.error("unsupported event", event);
      }
    }
  }
}).mount("#app")

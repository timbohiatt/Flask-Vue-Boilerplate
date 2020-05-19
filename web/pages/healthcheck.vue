<template>
  <div>
    <span>{{ healthcheck.message }}</span>
  </div>
</template>

<script>
export default {
  asyncData({ $axios, error }) {
    return $axios
      .get("/healthcheck")
      .then((response) => {
        console.log("Huston, We have Contact");
        return { healthcheck: response.data };
      })
      .catch((e) => {
        return { healthcheck: { message: "Huston, We have a problem!" } };
        error({
          status: 503,
          message: "API Server: Health Check Failed",
        });
      });
  },
};
</script>

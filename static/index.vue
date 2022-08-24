<template>
  <v-card
    color="white"
    class="mx-auto"
    max-width="1500"
    outlined
  >
     <v-container>
        <v-row dense>
          <v-col
            v-for="(item, i) in items"
            :key="i"
            cols="12"
          >
            <v-card
              :color="item.color"
              dark
            >
              <div class="d-flex flex-no-wrap">
                  <img
          :src="item.src"
          class="image"
          width="400"
          height="400"
        />

                <div>
                  <v-card-title
                    class="text-h1"
                    v-text="item.title"
                  ></v-card-title>

                  <v-card-subtitle v-text="item.artist"></v-card-subtitle>

                  <v-card-actions>
                    <v-btn
                      v-if="item.artist === 'Ellie Goulding'"
                      class="ml-2 mt-3"
                      fab
                      icon
                      height="40px"
                      right
                      width="40px"
                    >
                      <v-icon>mdi-play</v-icon>
                    </v-btn>

                    <v-btn
                      v-else
                      class="ml-2 mt-5"
                      outlined
                      rounded
                      small
                    >
                      START RADIO
                    </v-btn>
                  </v-card-actions>
                </div>
              </div>
            </v-card>
          </v-col>

           <v-col
            v-for="(item, i) in items2"
            :key="i"
            cols="4"
          >
            <v-card
              :color="item.color"
              dark
            >
              <div class="d-flex flex-no-wrap">

            <v-img :src="item.src" width="100" height="100"></v-img>

                <div>
                  <v-card-title
                    class="text-h5"
                    v-text="item.title"
                  ></v-card-title>

                  <v-card-subtitle v-text="item.artist"></v-card-subtitle>

                  <v-card-actions>
                    <v-btn
                      v-if="item.artist === 'Ellie Goulding'"
                      class="ml-2 mt-3"
                      fab
                      icon
                      height="40px"
                      right
                      width="40px"
                    >
                      <v-icon>mdi-play</v-icon>
                    </v-btn>

                    <v-btn
                      v-else
                      class="ml-2 mt-5"
                      outlined
                      rounded
                      small
                    >
                      START RADIO
                    </v-btn>
                  </v-card-actions>
                </div>
              </div>
            </v-card>
          </v-col>
        </v-row>
      </v-container>

  </v-card>
</template>

<script>
export default {
  name: 'IndexPage',
  data () {
    return {
      items: [
        {
          color: '#1F7087',
          src: '/icon.png',
          title: 'Supermodel text sample',
          artist: 'This document describes the REST-style version of PUG (Power User Gateway), a web interface for accessing PubChem data and services.'
        }],
      items2: [
        {
          color: '#1F7087',
          src: '@/assets/images/1-shoe.png',
          title: 'Supermodel text sample',
          artist: 'This document describes the REST-style version of PUG (Power User Gateway), a web interface for accessing PubChem data and services.'
        },
        {
          color: '#1F7087',
          src: '@/assets/images/2-shoe.png',
          title: 'Supermodel text sample',
          artist: 'This document describes the REST-style version of PUG (Power User Gateway), a web interface for accessing PubChem data and services.'
        },
        {
          color: '#1F7087',
          src: '@/assets/images/3-shoe.png',
          title: 'Supermodel text sample',
          artist: 'This document describes the REST-style version of PUG (Power User Gateway), a web interface for accessing PubChem data and services.'
        }]
    }
  }
}
</script>

<template>
  <div class="invoice-box">
    <table cellpadding="0" cellspacing="0">
      <h1 class="pb-2">Shopping Cart</h1>
      <tr class="heading">
        <td>Item</td>
        <td>Unit Cost</td>
        <td>Quantity</td>
        <td>Price</td>
      </tr>
      <tr v-for="item in items" :key="item" class="item">
        <td><input v-model="item.description"></td>
        <td>$<input v-model="item.price" type="number"></td>
        <td><input v-model="item.quantity" type="number"></td>
        <td>${{ item.price * item.quantity | currency }}</td>
      </tr>

      <tr>
        <td colspan="4">
          <v-btn color="blue" @click="addRow"> Add row</v-btn>
        </td>
      </tr>

      <tr class="total">
        <td colspan="3" />
        <td>Total: ${{ total | currency }}</td>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  name: 'InspirePage',
  filters: {
    currency (value) {
      return value.toFixed(2)
    }
  },
  transition: 'home',
  data () {
    return {
      items: [
        { description: 'Book 1', quantity: 1, price: 10 },
        { description: 'Book 2', quantity: 1, price: 15 },
        { description: 'Music CD', quantity: 1, price: 20 },
        { description: 'Small Chocolate', quantity: 1, price: 5 },
        { description: 'Big Chocolate', quantity: 1, price: 12 },
        { description: 'Headache Pills', quantity: 1, price: 15 },
        { description: 'Cold Syrup', quantity: 1, price: 15 },
        { description: 'Mobile Phone', quantity: 1, price: 100 },
        { description: 'Laptop', quantity: 1, price: 450 },
        { description: 'Perfume', quantity: 1, price: 35 }
      ]
    }
  },
  computed: {
    total () {
      return this.items.reduce(
        (acc, item) => acc + item.price * item.quantity,
        0
      )
    }
  },
  methods: {
    addRow () {
      this.items.push({ description: '', quantity: 1, price: 0 })
    }
  }
}
</script>
<style>
.invoice-box {
  max-width: 800px;
  margin: auto;
  padding: 30px;
  border: 1px solid #eee;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.15);
  font-size: 16px;
  line-height: 24px;
  font-family: "Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;
  color: #555;
}

.invoice-box table {
  width: 100%;
  line-height: inherit;
  text-align: left;
}

.invoice-box table td {
  padding: 5px;
  vertical-align: top;
}

.invoice-box table tr td:nth-child(n + 2) {
  text-align: right;
}

.invoice-box table tr.top table td {
  padding-bottom: 20px;
}

.invoice-box table tr.top table td.title {
  font-size: 45px;
  line-height: 45px;
  color: #333;
}

.invoice-box table tr.information table td {
  padding-bottom: 40px;
}

.invoice-box table tr.heading td {
  background: #eee;
  border-bottom: 1px solid #ddd;
  font-weight: bold;
}

.invoice-box table tr.details td {
  padding-bottom: 20px;
}

.invoice-box table tr.item td {
  border-bottom: 1px solid #eee;
}

.invoice-box table tr.item.last td {
  border-bottom: none;
}

.invoice-box table tr.item input {
  padding-left: 5px;
}

.invoice-box table tr.item td:first-child input {
  margin-left: -5px;
  width: 100%;
}

.invoice-box table tr.total td:nth-child(2) {
  border-top: 2px solid #eee;
  font-weight: bold;
}

.invoice-box input[type="number"] {
  width: 60px;
}

@media only screen and (max-width: 600px) {
  .invoice-box table tr.top table td {
    width: 100%;
    display: block;
    text-align: center;
  }

  .invoice-box table tr.information table td {
    width: 100%;
    display: block;
    text-align: center;
  }
}

/** RTL **/
.rtl {
  direction: rtl;
  font-family: Tahoma, "Helvetica Neue", "Helvetica", Helvetica, Arial,
    sans-serif;
}

.rtl table {
  text-align: right;
}

.rtl table tr td:nth-child(2) {
  text-align: left;
}

</style>

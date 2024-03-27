<template>
  <div class="image-actions">
    <div class="image-action">
      <img src="@/assets/waterbottle.png" alt="Bottle Image" @click="$emit('add-bottle', $refs.bottlePicker.value)" />
      <button class="child bottle" @click="$emit('add-bottle', $refs.bottlePicker.value)">Add bottle!</button>
      <select ref="bottlePicker" name="bottle" class="child bottle" id="bottlepicker">
        <option value="pick">Pick a bottle!</option>
        <option value="dp8">Disposable Plastic 8oz</option>
        <option value="dp12">Disposable Plastic 12oz</option>
        <option value="dp16.9">Disposable Plastic 16.9oz</option>
        <option value="rp17">Reusable Plastic 17 oz</option>
        <option value="rp25">Reusable Plastic 25 oz</option>
        <option value="rm12">Reusable Metal 12 oz</option>
        <option value="rm17">Reusable Metal 17 oz</option>
        <option value="rm25">Reusable Metal 25 oz</option>
      </select>
    </div>
    <div class="image-action">
      <img src="@/assets/leaf.png" alt="Leaf Image" @click="$emit('generate-score')" />
      <button class="child score" @click="$emit('generate-score')">Generate Score</button>
    </div>
    <div class="image-action">
      <img src="@/assets/saving.png" alt="Saving Image" @click="$emit('get-savings')" />
      <button class="child savings" @click="$emit('get-savings')">Click To Get Your Savings!</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ImageActions'
}
</script>

<style scoped>
.image-actions {
  display: flex;
  justify-content: center;
  gap: 20px;
}

.image-action {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 20px;
}

.image-action img {
  width: 100px;
  height: auto;
  cursor: pointer;
}

.image-action button {
  margin-top: 10px;
  padding: 8px 12px;
  border: 1px solid #ccc;
  border-radius: 5px;
  cursor: pointer;
}

.image-action select {
  margin-top: 10px;
  padding: 8px 12px;
  border: 1px solid #ccc;
  border-radius: 5px;
  cursor: pointer;
  width: 100%;
}

.image-action img {
  width: 150px;
  height: auto;
  cursor: pointer;
  margin: 0 10px;
}
</style>
<template>
  <div class="impact-calculator">
    <!-- Header -->
    <header>
      <h1>Impact Calculator</h1>
    </header>

    <!-- Image Actions -->
    <div class="image-actions">
      
      <div class="image-action">
        <img src="@/assets/waterbottle.png" alt="Bottle Image" @click="addBottle($refs.bottlePicker.value)" />
        <select ref="bottlePicker" name="bottle" class="child bottle" id="bottlepicker">
          <!-- Bottle options -->
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
        <img src="@/assets/leaf.png" alt="Leaf Image" @click="generateImpactScore()" />
        <!-- Removed the regular "Generate Score" button -->
        <div v-if="showImpactScore" class="results">
          <div id="scoreDisplay" class="display">{{ impactScore }}</div>
        </div>

      </div>

      <div class="image-action">
        <img src="@/assets/saving.png" alt="Saving Image" @click="getSavings()" />
        <!-- Removed the regular "Click To Get Your Savings!" button -->        
        <div v-if="showSavings" class="results">
          <div id="savingsDisplay" class="display">{{ savingsAmount }}</div>
        </div>
      </div>

    </div>

    <!-- Comment out or remove this section if it's the source of duplication -->
    <!-- <div class="results">
      <div id="scoreDisplay" class="display">{{ impactScore }}</div>
      <div id="savingsDisplay" class="display">{{ savingsAmount }}</div>
    </div> -->
  </div>
</template>

  
  <script>
  export default {
    name: 'ImpactCalculator',
    data() {
      return {
        bottleCounts: {
          'dp8': 0,
          'dp12': 0,
          'dp16.9': 0,
          'rp17': 0, 
          'rp25': 0,
          'rm12': 0,
          'rm17': 0,
          'rm25': 0
        },
        impactScore: '',
        savingsAmount: '',
        showImpactScore: false,
        showSavings: false,
      };
    },
    methods: {
      addBottle(bottleType) {
        if (bottleType !== "pick") {
          this.bottleCounts[bottleType]++;
          console.log(`${this.bottleCounts[bottleType]} ${bottleType} added.`);
          console.log("Current Bottle Counts:", this.bottleCounts);
        }
      },
      
      generateImpactScore() {
        // Points assigned to each bottle type
        const pointsPerBottle = {
          'dp8': 1,    // 8 oz bottle = 1 point
          'dp12': 3,   // 12 oz = 3 points
          'dp16.9': 5, // 16 oz = 5 points
          // The rest don't contribute to the total points
        };

        // Calculate the total impact score
        let score = 0;
        for (const bottleType in this.bottleCounts) {
          if (Object.hasOwnProperty.call(pointsPerBottle, bottleType)) {
            score += this.bottleCounts[bottleType] * pointsPerBottle[bottleType];
          }
        }

        // Update the impactScore state
        this.impactScore = score;
        console.log("Impact Score generated:", this.impactScore);

        // Show the impact score
        this.showImpactScore = true;
      },
      
      getSavings() {
        this.savingsAmount = "GENERATED SAVINGS";
        console.log("Savings Score generated");
        
        // Show the savings amount
        this.showSavings = true;
      },
    }
  }
  </script>
  
  <style scoped>
  /* Main layout and typography */
  .impact-calculator {
    font-family: 'Roboto', sans-serif;
    color: #333;
    background: #f0f0f0; /* Subtle background color for the whole calculator */
    padding: 2rem;
    border-radius: 10px;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
    max-width: 800px;
    margin: 2rem auto;
  }

  /* Header styles */
  header {
    background: linear-gradient(to right, #4CAF50, #8BC34A); /* Gradient background for the header */
    color: white;
    padding: 1rem 0;
    border-radius: 8px 8px 0 0;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    text-align: center;
    position: relative; /* For positioning the logo if needed */
  }

  h1 {
    margin: 0;
    font-size: 2.5rem; /* Larger font size for the title */
  }

  /* Adding a textured or patterned background to the top part with the logo */
  header::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-image: url('@/assets/background.png'); /* Path to your background texture or pattern */
    opacity: 0.2; /* Adjust the opacity to not overpower the header text */
    border-radius: 8px 8px 0 0;
  }
  
  /* Styles for Image Actions */
  .image-actions {
    display: flex;
    justify-content: center;
    flex-wrap: wrap; /* Wrap items on smaller screens */
    gap: 1rem; /* Spacing between action items */
    padding: 1rem; /* Padding within the actions container */
    background: white; /* White background for the action area */
    border-radius: 8px; /* Rounded corners for the action area */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Shadow for depth */
    margin-top: -1rem; /* Pull the action area up to overlap with the header */
  }


  .image-action {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 20px;
    width: 200px;
  }


  .image-action img {
    width: 150px;
    height: 150px;
    object-fit: cover;
    cursor: pointer;
    margin-bottom: 10px;
    transition: transform 0.1s, box-shadow 0.1s; /* Add box-shadow to the transition */
    border-radius: 10px; /* Optional: if you want rounded corners */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Soft shadow for depth */
  }

  /* Button-like styles for images */
  .image-action img:active {
    transform: scale(0.97); /* Slightly smaller scale for a subtle click effect */
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2); /* Smaller shadow for the pressed state */
  }


  .image-action button {
    margin-top: 10px;
    padding: 8px 12px;
    border: none; /* Remove border for a cleaner look */
    border-radius: 5px;
    cursor: pointer;
    width: 100%;
    transition: background-color 0.3s, transform 0.1s, box-shadow 0.1s; /* Add box-shadow to the transition */
    background-image: linear-gradient(to top, #f5f5f5, #ffffff); /* Subtle gradient effect */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Soft shadow for depth */
  }

  /* Button clicking effect */
  .image-action button:active {
    background-image: linear-gradient(to top, #e6e6e6, #f5f5f5); /* Darker gradient for the pressed state */
    transform: translateY(2px); /* Moves the button down to simulate a press */
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2); /* Smaller shadow for the pressed state */
  }

  .image-action select {
    padding: 10px 15px; /* Slightly larger padding for a touch-friendly interface */
    border: 2px solid #ccc; /* Solid border that matches the theme */
    border-radius: 5px; /* Rounded corners */
    background-color: white; /* Background color */
    font-size: 16px; /* Larger font size for better readability */
    cursor: pointer;
    width: 100%;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
    appearance: none; /* Remove default styling */
    background-image: 
      linear-gradient(45deg, transparent 50%, green 50%), 
      linear-gradient(135deg, green 50%, transparent 50%), 
      linear-gradient(to right, #fff, #fff); /* Custom arrow */
    background-position: 
      calc(100% - 20px) calc(1em + 2px), 
      calc(100% - 15px) calc(1em + 2px), 
      100% 0; /* Arrow position */
    background-size: 
      5px 5px, 
      5px 5px, 
      2.5em 2.5em; /* Arrow size */
    background-repeat: no-repeat;
    transition: border-color 0.3s ease-in-out, box-shadow 0.3s ease-in-out; /* Smooth transition for interactive states */
  }

  .image-action select:hover {
    border-color: #a5a5a5; /* Darken border on hover */
  }

  .image-action select:focus {
    border-color: #88c057; /* Green border color for focus */
    box-shadow: 0 0 8px rgba(136, 192, 87, 0.8); /* Glowing effect to match focus */
    outline: none; /* Remove the default focus outline */
  }


  /* Styles from Results.vue */
  .results {
    text-align: center;
    margin-top: 20px;
    font-family: 'Roboto', sans-serif;
  }


  .display {
    font-size: 24px;
    font-weight: bold;
    color: white; /* Default text color */
    background-color: #3a3a3c; /* Neutral dark background */
    padding: 12px 20px;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    margin: 10px 0;
    display: inline-block;
    animation: fadeInUp 0.5s ease-out;
  }

  #scoreDisplay {
    background-color: #4CAF50; /* Green for impact score */
  }

  #savingsDisplay {
    background-color: #2196F3; /* Blue for savings amount */
  }

  @keyframes fadeInUp {
    from {
      opacity: 0;
      transform: translateY(20px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }
  </style>
  
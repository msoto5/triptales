const quizData = [
/* Question format 
   {
        question: "Question",
        options: ["A1", "A2", "A3", "A4"],
        answers: {"A1":{"temp":1, "urban":-1}, 
                "A2":{"temp":1, "urban":1, "party":1}, 
                "A3":{"temp":1, "urban":1}, 
                "A4":{"urban":-2},
                }
    },
*/
    {
        question: "Does a holiday desitination need to be hot for you?",
        options: ["Absolutely", "Preferably", "Doesn't matter", "Prefer the cold"],
        answers: {"Absolutely":{"temp":2}, "Preferably":{"temp":1}, "Doesn't matter":{"temp":0}, "Prefer the cold":{"temp":-1}}
    },
    {
        question: "What outdoor holiday activity sounds the best?",
        options: ["Fun and games at the beach", "Relaxing by the pool", "Sightseeing in a city", "Exploring the wilderness"],
        answers: {"Fun and games at the beach":{"temp":1, "urban":-1}, 
                  "Relaxing by the pool (and the bar)":{"temp":1, "urban":1, "party":1}, 
                  "Sightseeing in a city":{"temp":1, "urban":1}, 
                  "Exploring nature":{"urban":2, "party":-1},
                }
    },
    {
        question: "What indoor holiday activity sounds the best?",
        options: ["Going to a wildlife museem", "Relaxing in a downtown bar with live music", "Clubbing!", "Night in a warm secluded winter cottage"],
        answers: {"Going to a wildlife museem":{"urban":-1, "party":-1}, 
                "Relaxing in a downtown bar with live music":{"urban":1, "party":1}, 
                "Clubbing!":{"temp":-1, "party":3}, 
                "Spending a night in a warm winters cottage in the countryside":{"urban":-2, "temp":-2, "party":-2},
                }
    },
    {
        question: "Is Partying and going out a big part of your holidays?",
        options: ["Absolutely", "Sometimes", "Doesn't matter", "Preferably not"],
        answers: {"Absolutely":{"party":2}, 
                "Sometimes":{"party":1},
                "Doesn't matter":{"party":0}, 
                "Preferably not":{"party":-2}, 
                }
    },
    {
        question: "Which of the following sounds like the worst way to spend your holiday",
        options: ["Out partying all night every night", "Exploring a packed city", "Relax in the sun for hours a day", "No opinion"],
        answers: {"Out partying all night every night":{"party":-3}, 
                "Exploring countryside away from everyone":{"urban":-3},
                "Relax in the sun for hours a day":{"temp":-3}, 
                "No opinion":{"urban":-1, "temp":-1, "party":-1},
                }
    },
    // Add more questions here...
  ];
  
  const questionElement = document.getElementById("question");
  const optionsElement = document.getElementById("options");
  
  let currentQuestion = 0;
  let temperature = 0;
  let urban = 0;
  let party = 0;

  let continent = "";
  let description = "";
  let image = "";
  
  function showQuestion() {
    const question = quizData[currentQuestion];
    questionElement.innerText = question.question;
  
    optionsElement.innerHTML = "";
    question.options.forEach(option => {
      const button = document.createElement("button");
      button.classList.add("answer-button")
      button.innerText = option;
      optionsElement.appendChild(button);
      button.addEventListener("click", selectAnswer);
    });
  }
  
  function selectAnswer(e) {
    const selectedButton = e.target;
    const answers = quizData[currentQuestion].answers;
  
    for (var response in answers) {
        if (selectedButton.innerText === response) {
            for (var scores in answers[response]) {
                if (scores == "temp") {
                    temperature = temperature + Number(answers[response][scores])
                }
                if (scores == "urban") {
                    urban = urban + Number(answers[response][scores])
                }
                if (scores == "party") {
                    party = party + Number(answers[response][scores])
                }
            }
        }
    }
  
    currentQuestion++;
  
    if (currentQuestion < quizData.length) {
      showQuestion();
    } else {
      showResult();
    }
  }
  
  function showResult() {
    if (temperature <= 0) {
        if (urban <= 0) {
            continent = "North America";
            description = "North America have some of the most underrated landscapes. The wilderness, mountain ranges and natural features are all breath taking. With many national parks to explore, you could keep yourself busy for a whole year. If you're adventureous, and can't quite handle the heat of other continents, then North America is a no brainer"
        } else if (party <= 0) {
            continent = "Asia";
            description = "Asia has some of the best cities in the whole world. You could spend weeks exploring these endless cities that have anything and everything you could imagine. If your looking for a relaxed and chill holiday, sightseeing in Asia is a fantastic idea"

        } else {
            continent = "Europe"
            description = "Tried and tested, Europe has it all. Managable temperatures, cities full of a rich and diverse culture, and trust me, they know how to party. You can do anything you could want to in Europe, so go have fun!"

        }
    } else {
        if (urban > 0) {
            continent = "Oceania";
            description = "Amazingly warm, amazing cities and an amazing nightlife, what else could you ask for? Oceania provides a unique blend of blistering hot weather, fantastic cities to explore and get lost in an otherworldly nightlife."
        } else if (party <= 0) {
            continent = "Africa";
            description = "Africa is the ideal place for a adventerous summer vaccation! Africa is world renouned for it's wildlife and terrain, and is the perfect destination for anyone looking for a quiet, but exciting adventure!"
        } else {
            continent = "South America"
            description = "South America is a fantastic blend of wonderful landscapes and an incredible nightlife. Anyone looking for a well rounded holiday, with endless activities to do during day and night, south america may be the destination for you!"

        }
    }

    quiz.innerHTML = `
      <h1>Quiz Completed!</h1>
      <h4>The results are in... your ideal holiday is.</h4>
      <br>
      <h1>A holiday to ${continent}!</h1>
      <h5>${description}</h5>
    `;
  }
  
  showQuestion();
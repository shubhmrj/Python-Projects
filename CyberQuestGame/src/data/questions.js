const questions = {
  "Password Safety": [
    {
      question: "Which password is the strongest?",
      options: [
        { text: "password123", correct: false },
        { text: "P@ssw0rd!2025", correct: true },
        { text: "qwerty", correct: false },
        { text: "123456", correct: false }
      ],
      explanation: "Strong passwords use a mix of letters, numbers, and symbols."
    },
    {
      question: "What should you avoid when creating a password?",
      options: [
        { text: "Using your birthdate", correct: true },
        { text: "Using a random phrase", correct: false },
        { text: "Using symbols", correct: false },
        { text: "Using both upper and lower case letters", correct: false }
      ],
      explanation: "Personal information is easy to guess or find."
    }
  ],
  "Phishing Awareness": [
    {
      question: "What is a common sign of a phishing email?",
      options: [
        { text: "Spelling mistakes and urgent requests", correct: true },
        { text: "A friendly greeting", correct: false },
        { text: "Your name in the email", correct: false },
        { text: "A known sender address", correct: false }
      ],
      explanation: "Phishing emails often contain errors and pressure to act quickly."
    },
    {
      question: "What should you do if you suspect a phishing attempt?",
      options: [
        { text: "Click the link to check", correct: false },
        { text: "Delete or report the email", correct: true },
        { text: "Reply asking for more info", correct: false },
        { text: "Forward to friends", correct: false }
      ],
      explanation: "Never interact with suspicious emails; report or delete them."
    }
  ],
  "Malware Detection": [
    {
      question: "What is malware?",
      options: [
        { text: "Malicious software", correct: true },
        { text: "A type of hardware", correct: false },
        { text: "A secure website", correct: false },
        { text: "An antivirus program", correct: false }
      ],
      explanation: "Malware is software designed to harm your device or data."
    },
    {
      question: "Which action can help avoid malware?",
      options: [
        { text: "Opening email attachments from unknown senders", correct: false },
        { text: "Clicking pop-up ads", correct: false },
        { text: "Installing software from trusted sources", correct: true },
        { text: "Ignoring software updates", correct: false }
      ],
      explanation: "Install software only from reputable sources."
    }
  ],
  "Online Privacy": [
    {
      question: "Which info should you avoid sharing online?",
      options: [
        { text: "Your home address", correct: true },
        { text: "A favorite color", correct: false },
        { text: "A hobby", correct: false },
        { text: "A nickname", correct: false }
      ],
      explanation: "Personal details like your address should be kept private."
    },
    {
      question: "How can you improve your online privacy?",
      options: [
        { text: "Use strong, unique passwords", correct: true },
        { text: "Share passwords with friends", correct: false },
        { text: "Post your schedule publicly", correct: false },
        { text: "Accept all cookies on every website", correct: false }
      ],
      explanation: "Unique passwords and careful sharing improve privacy."
    }
  ]
};

export default questions;

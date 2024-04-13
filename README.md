## Branch
Please check version 1 and 2 for branches where our application was developed.

## Video Link to web application
The video link to how the application works: https://github.com/pxd222PranavDhinakar/Green-Wave/assets/118007706/43f31535-719c-4fe5-a7e7-846904f29468

## Git Workflow Useful Rules (Not Strict)

To maintain the integrity and quality of our codebase, we follow a structured process for contributing changes. Please adhere to the steps outlined below to ensure your contributions can be efficiently reviewed and integrated.

### 1. Setup Your Environment

Before you start, make sure you have a GitHub account, have Git installed on your local machine, and have access to our repository. If you're new to Git, consider reading through the [Git documentation](https://git-scm.com/doc) to familiarize yourself with basic concepts.

### 2. Clone the Repository

If you haven't already, clone the repository to your local machine using:

```bash
git clone https://github.com/your-organization/your-repository.git
cd your-repository
```

### 3. Create a New Branch

For each new set of changes or feature you're working on, create a new branch off of the `main` (or `master`, depending on your repo setup) branch. Use a descriptive name for your branch that briefly describes the changes or feature.

```bash
git checkout -b feature/your-feature-name
```

### 4. Make Your Changes

Implement your changes in your local repository. Keep your commits small and focused; each should represent a logical unit of work. Use meaningful commit messages to describe the changes made.

```bash
git add .
git commit -m "A descriptive message explaining your change"
```

### 5. Keep Your Branch Updated

Regularly pull changes from the `main` or `master` branch into your feature branch to stay up to date and resolve any merge conflicts early.

```bash
git checkout main
git pull origin main
git checkout feature/your-feature-name
git merge main
```

### 6. Push Your Changes

Once you're ready to share your work, push your branch to the GitHub repository.

```bash
git push -u origin feature/your-feature-name
```

### 7. Create a Pull Request (PR)

Go to the repository on GitHub, and you'll see a prompt to create a pull request for your branch. Click the "Compare & pull request" button, fill in the details of your changes, and submit it. Ensure your PR description clearly describes the problem you're solving and any relevant details reviewers might need.

### 8. Review and Revise

Your PR will be reviewed by one or more team members. Be open to feedback and ready to make revisions. Continuous integration checks and other automated tests should run against your PR to ensure quality and compatibility.

### 9. Merge Your Changes

Once your PR is approved and passes all checks, it can be merged into the main branch. Typically, the person who approves your PR will merge it, but follow your team's protocol if different.

### 10. Clean Up

After your changes have been merged, you can safely delete your feature branch from both your local machine and the GitHub repository.

```bash
git branch -d feature/your-feature-name
git push origin --delete feature/your-feature-name
```

### Additional Guidelines

- **Code Review**: All changes must go through a code review process. Be constructive with your feedback and responsive to comments on your PRs.
- **Testing**: Ensure your changes are thoroughly tested before submitting a PR. Include unit tests where applicable.
- **Documentation**: Update any relevant documentation as part of your changes, including this README if necessary.

Adhering to this protocol helps us maintain a clean, stable, and efficient workflow, ensuring our project remains high-quality and collaborative. Thank you for contributing!

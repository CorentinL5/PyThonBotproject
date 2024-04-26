<a href="https://wakatime.com/badge/user/579bed4b-39bc-4178-85cd-cca984453d63/project/dd8e59b0-cfad-48a8-a0f0-c1341fad7612">
   <img align="right" src="https://wakatime.com/badge/user/579bed4b-39bc-4178-85cd-cca984453d63/project/dd8e59b0-cfad-48a8-a0f0-c1341fad7612.svg" alt="wakatime">
</a>
<img align="left" src="assets/images/BotPy.png" width="69em">

# PyThonBotproject

PyThonBotproject is a small Python project created for fun, with the aim of learning how to use the discord.py library to create Discord bots.

## Installation

To run this project, you will need to install the discord.py library. You can do this by executing the following command in your terminal:
```
pip install discord
```

> [!IMPORTANT]
> Make sure you also have a `token.txt` file containing the token for your Discord bot.

## Configuration

1. **Install Dependencies:** Run `pip install -r assets/requirements.txt` to install all necessary dependencies.

2. **Get a Discord Token:** Visit the [Discord Developer Portal](https://discord.com/developers/applications) to create a new application.
<br>Then, add a bot to this application and **copy the generated token**.
   
3. **Create a `token.txt` File:** Create the file in the [`assets/`](assets) directory of your project and paste the Discord bot token there.
> [!WARNING]
> Avoid committing your `token.txt` file to a public repository to prevent unauthorized access to your Discord bot.

## Usage

1. **Run the Bot:** Use your terminal to navigate to the directory containing the main Python file of your bot. Then, execute the following command:
    ```
    python bot.py
    ```

2. **Invite the Bot to Your Discord Server:** Use the invitation link generated by the Discord Developer interface to add your bot to your Discord server.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please create an issue to discuss the changes you'd like to make.

## License

This project is distributed under the MIT license. See [LICENSE](LICENSE) for more information.

---

> [!NOTE]
> Bases for python codes are comming from [discord.py](https://discordpy.readthedocs.io/en/stable/index.html) documentation.

> [!CAUTION]
> Be careful when granting permissions to your Discord bot. Only give it the permissions it needs to function properly to avoid potential security risks.

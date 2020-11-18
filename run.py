def main():
    try:
        from vkwave.bots import SimpleLongPollBot
        
    except ImportError as exc:
        raise ImportError(
            "Couldn't import VkWave. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    from bot.bot import bot
    bot.run_forever()

if __name__ == '__main__':
    main()
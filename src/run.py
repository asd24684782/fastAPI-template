import uvicorn
from config.EnumApp import AppEnum

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=AppEnum.PORT.value, reload=True, log_level="debug", debug=True)
from typing import cast
import uvicorn
from decouple import config

if __name__ == '__main__':
    port = config('PORT', cast=int)
    uvicorn.run("application:app", host="0.0.0.0", port=port, reload=True, debug=True)
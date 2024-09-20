# Use Node.js base image
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json (if available) for better caching
COPY package.json ./
# Uncomment the line below if you have a package-lock.json
# COPY package-lock.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Expose port 3000 for the Node.js app
EXPOSE 3000

# Start the Node.js server
CMD ["node", "app.js"]

import fs from 'fs'
import path from 'path'
import matter from 'gray-matter'

const postsDirectory = path.join(process.cwd(), 'posts')

export async function getSortedPostsData() {
    // fetch post data from an external API endpoint
    const res = await fetch('..')
    return res.json()
  }